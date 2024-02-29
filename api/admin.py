from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from api.forms import RegisterForm, CustomerForm, MessagesForm
from database.models import User, Organization, Customer, Messages, Dialogue, Contact, Agent
from import_export import resources, fields, widgets
from import_export.admin import ImportExportModelAdmin
from django.core.exceptions import ValidationError
from database.validators import validate_tg_nickname


class CustomerOrganization(admin.TabularInline):
    model = Customer.organizations.through


class OrganizationAgent(admin.TabularInline):
    model = Agent.organizations.through

    
class OrganizationContact(admin.TabularInline):
    model = Contact.organization.through

    
class MessagesInline(admin.TabularInline):
    model = Messages
    form = MessagesForm
    fk_name = 'dialogue_id'
    fields = ('sender_type', 'source', 'message', 'ctime',)
    readonly_fields = ('ctime',)
    ordering = ('ctime',)
    extra = 1
    can_delete = False

    def has_change_permission(self, request, obj=None):
        return False



class OrganizationAdmin(admin.ModelAdmin):
    model = Organization
    inlines = [OrganizationContact, CustomerOrganization, OrganizationAgent,]


class CustomUserAdmin(BaseUserAdmin):
    add_form = RegisterForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name', 'email', 'password1', 'password2', 'tg_id', 'tg_nickname', 'organization'),
        }),
    )

    fieldsets = (
        (None, {'fields': ('full_name', 'email', 'password', 'organization')}),
        ('Telegram', {'fields': ('tg_id', 'tg_nickname')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    )

    list_display = ('id', 'full_name', 'email', 'organization', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    list_display_links = ('id', 'full_name')
    ordering = ('id',)


class CustomerResource(resources.ModelResource):
    organizations = fields.Field(
        attribute='organizations',
        column_name='organizations',
        widget=widgets.ManyToManyWidget(Organization, field='title')
    )

    class Meta:
        model = Customer
        fields = ('id', 'full_name', 'tg_id', 'tg_nickname')
        export_order = ('id', 'full_name', 'tg_id',
                        'tg_nickname', 'organizations')

        
    def before_import_row(self, row, **kwargs):
        tg_nickname = row.get('tg_nickname', '')
        try:
            validate_tg_nickname(tg_nickname)
        except ValidationError as e:
            raise ValidationError(f"Error in row #{kwargs['row_number']}: {e}")


class CustomerAdmin(ImportExportModelAdmin):
    form = CustomerForm
    resource_class = CustomerResource

    list_display = ('id', 'full_name', 'tg_id', 'tg_nickname', 'ctime',)
    list_filter = ('organization',)
    list_display_links = ('id', 'full_name',)
    ordering = ('id',)


class DialogueAdmin(admin.ModelAdmin):
    model = Dialogue
    inlines = [MessagesInline]
    list_display = ('organization', 'customer', 'ctime',)
    list_filter = ('organization', 'customer',)
    list_display_links = ('organization', 'customer',)
    ordering = ('id',)

    
admin.site.register(User, CustomUserAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Agent)
admin.site.register(Contact)
admin.site.register(Messages)
admin.site.register(Dialogue, DialogueAdmin)
