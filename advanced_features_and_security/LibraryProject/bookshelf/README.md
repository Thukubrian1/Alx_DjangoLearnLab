# Documentation in README.md

    """
    Permissions and Groups Setup
============================
    1. Custom Permissions:
        - Added to `CustomModel` with the following permissions:
        - can_view: View instances
        - can_create: Create instances
        - can_edit: Edit instances
        - can_delete: Delete instances

    2. Groups:
        - Editors: Assigned can_create and can_edit permissions.
        - Viewers: Assigned can_view permission.
        - Admins: Assigned all permissions.

    3. Views:
        - Protected with `@permission_required` decorator to enforce access control.
        - Example Views:
        - `view_custom_model`
        - `create_custom_model`
        - `edit_custom_model`
        - `delete_custom_model`

    4. Testing:
        - Create test users and assign them to the groups (Editors, Viewers, Admins).
        - Verify access control by attempting to perform actions restricted by permissions.
    """