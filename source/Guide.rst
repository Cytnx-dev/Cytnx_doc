User Guide
=================================
To use the library, simply include/import cytnx. 

* In Python, using import:

.. code-block:: python
    :linenos:

    import cytnx

* In C++, using the include header:

.. code-block:: c++
    :linenos:

    #include "cytnx.hpp";


.. Note::
    In C++, there is a namespace **cytnx**. 

Aliases in Python modules and C++ namespaces can be used equivalently, for example if we want to alias cytnx as cy, 

* In Python:

.. code-block:: python
    :linenos:

    import cytnx as cy

This is equivalent in C++ to:

* In C++:

.. code-block:: c++
    :linenos:

    #include "cytnx.hpp";
    namespace cy=cytnx;
    

**Now we are ready to start using cytnx!**

**How to use this guide**

This guide explains the main functions and application programming interfaces (APIs) of Cytnx. We start with general remarks on the behavior of objects in Cytnx. We recommend all new users to read this chapter on *Object behavior* first. Then, we explain the different classes and functions. The order of the topics is from bottom-up, with the most basic objects explained first, before high level structures are introduced. Users who want to get a good understanding of the library can thus read from start to end. For others, who want to use Cytnx without digging too deep into the technical details, we recommend to skip the chapters **Device**, **Tensor**, **Storage** and **Scalar** and start with the explanation of **UniTensor**. The other chapters can later be revisited if the corresponding more specialized functionality is needed. For example, if a GPU shall be used, the reader can jump back to the chapter explaining *Device*. Or, if complex data types are required, one can read the chapter about *Scalar*.

A **UniTensor** is the central object of Cytnx and implements a tensor with its properties. These include for example the tensor elements, indices, index labels and possibly symmetries of the tensor. The underlying data structure is a **Tensor** object, but users typically do not have to deal with this object directly. Instead, a **UniTensor** can be manipulated directly and be used in contractions or linear algebra functions.

For a comprehensive list of classes, functions and methods and their arguments and usage, see the `API documentation <https://kaihsinwu.gitlab.io/cytnx_api/>`_.

Continue reading:

.. toctree::
    :maxdepth: 3
    :numbered:

    guide/behavior.rst
    guide/Device.rst
    guide/basic_obj/Tensor.rst
    guide/basic_obj/Storage.rst
    guide/basic_obj/Scalar.rst
    guide/TNotation.rst
    guide/uniten.rst
    guide/contraction.rst
    guide/linalg.rst
    guide/itersol.rst
    .. guide/xlinalg.rst

    guide/common.rst
