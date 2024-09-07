/*
This is an example of a very basic .cs file. All files with C# code have the .cs extension.

A C# project must always contain at least 1 namespace. A namespace is an environment in which the compiler reads all your code. It helps to group your code and make it more versatile when you import it into other projects.

Inside the namespace we define a new class called Program. A class is a place where you can define a group of related variables and functions. C# forces us to put all of our code inside a class.

Inside the Program class we are defining the main function of our program. This is where our code will start (called the entry-point). We will worry about the "string[] args" later. It is in here where we put our code.
*/

// We have to import the System namespace (provided by Windows) in order to have access to classes such as Console (used below)
using System;

namespace YourNamespace
{
    class Program
    {
        static void Main(string[] args)
        {
            // Prints "Hello World!" to the console.
            Console.WriteLine("Hello World!");
        }
    }
}

/*
In order to compile and run our code:
- If you're using an IDE such as Visual Studio:
- - There's probably a button to start the program. It will do everything for you.
- If you're using the command line:
- - Type "cd /" to return to the top of the drive. It should say "C:\>"
- - Type "cd Windows/Microsoft.NET/Framework/v4.0*". It should say "C:\Windows\Microsoft.NET\Framework\v4.0.30319>"
- - Type "csc.exe " and then the directory and name of your file (e.g. "C:\Users\USER\your-folder\file.cs"
- - Double click on the .exe file that is created in the directory you specified
*/
