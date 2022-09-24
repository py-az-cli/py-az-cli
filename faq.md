# What is py-az-cli?

Py-az-cli is an open-source project based on the Azure CLI (az or azcli) that is a nice tool for automating things in the Microsoft Azure Cloud.

The reason for this project is to provide a pythonic wrapper to the Azure CLI so that developers can automate Azure using pure python.

# Why not just use the Azure Python SDK?

Have you tried programming Azure automation with the Python SDK?  If you have, you know that it is a thin wrapper over the Azure REST API.  And it is not fun to use.  The REST API is designed to follow REST principles and not necessarily usability principles, nor pythonic principles.  

The Azure CLI on the other hand is much more intuitive, and designed more of the style of the Unix philosophy as an easy to use command line interface.  It is great for use when interacting with Azure using the Shell.  However Shell programming is not necesarily easy, nor is it normally considered a full programming language.

So py-az-cli brings the Azure CLI together with Python to have the best of both worlds: A easy to use and intuitive API that can be programmed from an easy to use and intuitive language, Python.

# How does it work?
The py-az-cli python module is a code-generated library that acts a generator and executor of az command line commands.  It is totally dependent on the Azure CLI being installed.  These commands are run by the Azure CLI on the client machine.   In a nutshell, any python commands run from py-az-cli are translated back into the Azure CLI syntax and executed, and then the output of the command is returned to the calling Python module in the form of a Python dictionary (instead of the native Azure CLI Json).   

For example, the following is the Azure CLI syntax for creating a storage account:
```
az storage account create --name mystorageaccount --resource-group myresourcegroup
```
Here's the py-az-cl equivalent:
```
import pyaz
pyaz.storage.account.create(name="mystorageaccount", resource_group="myresourcegroup")
```
As you can see, the py-az-cli version is slightly more verbose, but it has a number of advantages over the Azure CLI:
- You can automate Azure using the same commands as the Azure CLI but in a Pythonic manner
- There is built-in intellisense when using modern IDE, which provides lists of arguments and commands available, making it much easier to learn the APIs
- The dot notation for the commands and subcommands is intuitive and easy to navigate
- It's much more fun to program with py-az-cli

