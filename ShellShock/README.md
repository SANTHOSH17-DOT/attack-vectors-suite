Facing the Shellshock Vulnerability

![image](https://user-images.githubusercontent.com/70282840/194763109-a8b937e9-2b71-4e69-8b8f-32c10f888af7.png)

Since the things we added are strange when parsed to the command grep, it won't understand them.
Now, what if we add some stuff after the function?

![image](https://user-images.githubusercontent.com/70282840/194763129-912f247f-90e6-4620-ab21-597cf55faa09.png)

Did you notice that echo NOOOOOOOOOOOOOOO! was executed normally? This is the Shellshock bug!

This works because when the new shell sees an environment variable beginning with (), it gets the variable name and executes the following string. This includes executing anything after the function, i.e, the evaluation does not stop when the end of the function definition is reached!

Remember that echo is not the only thing we can do

![image](https://user-images.githubusercontent.com/70282840/194763159-5aeedf95-db9c-4f5c-b154-8631fd5db662.png)

we actually don't need to use a system environment variable nor even call a real command:

![image](https://user-images.githubusercontent.com/70282840/194763180-31ab5980-7a26-4614-9c98-6dd1af242e93.png)
