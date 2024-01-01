"""
1. What's the Class and what's the Object
    - Class is a model/template and Object is a sample derived from the model(class)
    - CLASS will have 'ATTRIBUTE' (description) - variables, instance variables
    - they are global variables
    - these variables are changeable if they are defined in constructor '__init__'


2. What is the difference between class and object?
    - Class is a template, a model; and Object is the instance which is created using that template/model (class).
    - Instance of a class is object: sample that was created based on the class is called object.
    - Object is specific whereas class is general
    - using a class we can create many objects/instances

3. Why do we use a Class and why do we use an Object?
    - we use Class to define global/general attributes, behavior/actions and description of something or somewhat
    - than that class/model can be used while INSTANCIATION, i.e. we use Class for the creation of an Object
    - Object uses class attributes and defines certain parameters also called instance variables
    - we can use single class attributes for a multiple objects creation,i.e. multiple instanciations

4. CONSTRUCTOR (of the class when you instantiate) >>> we need it in the Class to make it easier to customize attributes
    # __init__ function will override the global variable values (name='pushka', breed='no breed')
    # everything defined in the Constructor does not have to be defined in the Class Global variable!!!
    # if the attribute is defined in the Constructor than later while instantiating we wouldn't have to update >>>
         >>> any of the default variables in the separate line
    # for example: if we define 'name' in the constructor than later there is no need to assign a new value to the 'name' for an object
    # it means we don't have to write: "dog1.name = 'charlie'"; instead we will just include it in the 'Dog' class while creating a new object:
        # dog1 = Dog('charlie', ...) >> and there is no need for an extra line: dog1.name  = 'charlie'

5. What is Encapsulation?
    - the purpose is to hide certain attributes from the object
    - to set some restrictions based on business logic
    - __variable/attribute name >> to encapsulate
    - for example: "__mileage" on the car >> we set a restriction from intentional/unintentional attempts to change mileage value on the car

6. What is Inheritance and why do we use it?
    - we use inheritance while creating a new class and using existing class's attributes and behaviors to minimiza redunduncy
    - inheritance created parent-child relationship where child class inherits all attributes from the parent
    - child class has access to the parent class but parent class doesn't have any access
    - for example: we created class Car and then when we were creating a new class Electric_Car we inheritted attributes from class Car
    - then we added some new attributes and behaviors pertaining to the Elecetric car
    - those new attributes are not accessable for the parent class Car

7. What is a function overriding, also called a Polymorphism?
    - when we need to make some changes to the certain function
    - function overriding happens in child class
    - for example: after inherriting from the parent class Car we overrided a function called 'fill_tank' in the child class Electric_car
    -




"""