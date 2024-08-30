class ClassGenerator:
    @staticmethod
    def generate_class(class_name, method_name='run'):
        return f'{class_name}.{method_name}'
