from app.data.models.model_imports import *
import app.data.databuilder.utils.generator as gen
import app.data.repository.table_functions as tf


class GenCategory:
    def __init__(self):
        self.Name = gen.get_random_word()
        random_row = tf.get_random_row(Category)
        self.ParentId = getattr(random_row, "Id", None)


if __name__ == '__main__':
    cat = GenCategory()
    print(cat.__dict__)

