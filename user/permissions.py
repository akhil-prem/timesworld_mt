def is_student_or_admin(user):
    return user.role == 'student' or user.role == 'admin'


def is_staff_or_admin(user):
    return user.role == 'staff' or user.role == 'admin'


def is_editor_or_admin(user):
    return user.role == 'editor' or user.role == 'admin'


def is_admin(user):
    return user.role == 'admin'
