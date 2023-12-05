THE HBNB PROJECT

The goal of the project is to deploy on our server a simple copy of the AirBnB website. In this project we will be implementing several components like:
A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
A website (the front-end) that shows the final product to everybody: static and dynamic
A database or files that store data (data = objects)
An API that provides a communication interface between the front-end and our data (retrieve, create, delete, update them)

We shall build this project step-by-step beginning with:

- The Console --> This first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from our console code (the command interpreter itself) and from the front-end and RestAPI we will build later, we won’t have to pay attention (take care) of how our objects are stored.
  This abstraction will also allow us to change the type of storage easily without updating all of our codebase.
  The console will be a tool to validate this storage engine.

- Web static
  HTML/CSS
  create the HTML of your application
  create template of each object

- MySQL storage
  replace the file storage by a Database storage
  map our models to a table in database by using an O.R.M.

- Web framework - templating
  create our first web server in Python
  make our static HTML file dynamic by using objects stored in a file or database

- RESTful API
  expose all our objects stored via a JSON web interface
  manipulate our objects via a RESTful API

- Web dynamic
  learn JQuery
  load objects from the client side by using our own RESTful API

- Files and Directories
  models directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
  tests directory will contain all unit tests.
  console.py file is the entry point of our command interpreter.
  models/base_model.py file is the base class of all our models. It contains common elements:
  attributes: id, created_at and updated_at
  methods: save() and to_json()
  models/engine directory will contain all storage classes (using the same prototype). For the moment you will have only one: file_storage.py.

- Storage
  Persistency is really important for a web application. It means: every time our program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.

  In this project, we will manipulate 2 types of storage: file and database. For the moment, you will focus on file.

  Why separate “storage management” from “model”? It’s to make our models modular and independent. With this architecture, we can easily replace our storage system without re-coding everything everywhere.

  we will always use class attributes for any object. Why not instance attributes? For 3 reasons:

  Provide easy class description: everybody will be able to see quickly what a model should contain (which attributes, etc…)
  Provide default value of any attribute
  In the future, provide the same model behavior for file storage or database storage
