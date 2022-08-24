from .permissions import IsStaffEditorPermission


class StaffEditorPermissionMixin():
  permission_classes = [    
    IsStaffEditorPermission
  ]
  