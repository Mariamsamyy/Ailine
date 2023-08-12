from django.contrib.auth.models import User
from django.contrib.auth.models import Group

def assign_quality_control_manager_role(user):
  """Assigns the quality control manager role to the given user."""

  group = Group.objects.get(name='Quality Control Manager')
  group.user_set.add(user)

def create_new_customer_service_user(username, password):
  """Creates a new user for a new customer service."""

  user = User.objects.create_user(username, password)
  user.is_active = True
  user.save()

def disable_customer_service_account(user):
  """Disables the customer service account for the given user."""

  user.is_active = False
  user.save()

def enable_customer_service_account(user):
  """Enables the customer service account for the given user."""

  user.is_active = True
  user.save()
