import gc
import weakref

from django.db.migrations.state import ModelState, ProjectState

from .models import MyModel


def test_rendered_migration_state_is_released():
    project_state = ProjectState()
    project_state.add_model(ModelState.from_model(MyModel))
    rendered_model = weakref.ref(project_state.apps.get_model('tests', 'MyModel'))

    del project_state
    gc.collect()

    assert rendered_model() is None
