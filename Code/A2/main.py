from utils.extract_class_names import ClassNameListener
from  utils.extract_method_names import MethodNameListener
from  utils.extract_variable_names import VariableNameListener
from utils.get_java_files import get_files
from utils.path import Path

# set the path in utils/path.py before you run it

if __name__ == '__main__':
    files = get_files(Path.project_path)
    for file in files:
        print(f"File Name: " + file.split('\\')[-1])

        class_names = ClassNameListener.run_file(file)
        print("Class names: ")
        print(class_names)

        method_names = MethodNameListener.run_file(file)
        print("Method names: ")
        print(method_names)

        variable_names = VariableNameListener.run_file(file)
        print("Variable names: ")
        print(variable_names)

        print("*****************************************\n")




