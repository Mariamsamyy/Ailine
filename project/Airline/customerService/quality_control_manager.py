from django.contrib.auth.models import Group

class QualityControlManager(Group):
  """A group for quality control managers."""

  permissions = [
      'customer_service.can_assign_quality_control_manager_role',
      'customer_service.can_create_new_customer_service_user',
      'customer_service.can_disable_customer_service_account',
      'customer_service.can_enable_customer_service_account',
  ]