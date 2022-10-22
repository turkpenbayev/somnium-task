from rest_framework import routers

from .views import DepartmentPersonalPostionViewSet, OrganizationViewSet, PersonalTaskViewSet, PersonalViewSet, PositionViewSet, DepartmentViewSet

router = routers.SimpleRouter()
router.register('manage/organizations',
                OrganizationViewSet, 'manage_organizations')
router.register('manage/personals', PersonalViewSet, 'manage_personals')
router.register('manage/positions', PositionViewSet, 'manage_positions')
router.register('manage/departments', DepartmentViewSet, 'manage_departments')
router.register('manage/department-personals',
                DepartmentPersonalPostionViewSet, 'manage_department_personals')
router.register('manage/personal-tasks',
                PersonalTaskViewSet, 'manage_personal_tasks')

urlpatterns = [
    *router.urls,
]
