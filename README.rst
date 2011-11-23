ParseMeFoo
==========


What is this?
-------------

ParseMeFoo is a simple parse game/challenge where the challenges is
made in python but you can solve them using any method you want.

A challenge can be everything that can be parsed using line by line
parsing. Typical log files, commandline output, and other places where
you need to get a better overview from a higher perspective..


How does it work?
-----------------

ParseMeFoo will generate a list of 10 lines. It is upto the challenge
itself to choose how that line will look like, and it can be
everything from a word, to a long sentence.. The challenge also knows
how the line should look like if you did the right thing to it.


Example
-------

 $ ./parsemefoo basic_swapper help
 Usage: ./parsemefoo basic_swapper [start | done | help]
 
 ## Example output ##
 SYJJBCYF I2JMT997
 J1GS6B23 AADKAYOJ
 SGBEVOG4 18TM9XBD
 IIW3D64A 26TDUV1H
 
 ## Example input ##
 I2JMT997 SYJJBCYF
 AADKAYOJ J1GS6B23
 18TM9XBD SGBEVOG4
 26TDUV1H IIW3D64A

 $ ./parsemefoo basic_swapper start | awk {' print $2" "$1 '} | ./parsemefoo basic_swapper done
 You did it!

 $ ./parsemefoo list
 solved:
   basic_swapper (A basic wordswap challenge)
 
 unsolved:
   basic_upperme (Easy challenge which wants uppercase input)
   dummy (Dummy challenge which outputs the solution)


Contribute
----------

One of the best things with ParseMeFoo is that it is supereasy to
create your own challenges and contribute to the project.

Copy the dummy.py file in the challenges folder and edit it..

Here is one of the simplest challenges called upperme.

 class Challenge:
     author = 'Your Name'
     description = 'Easy challenge which wants uppercase input'
 
     def generate(self):
         return 'uppercaseme'
 
     def parse(self, line):
         return line.upper()

For each line it generates using the generate() function, it will
automaticly run it trough the parse() function and use the output to
judge your job. This is all you haveto do to make a challenge,
generate some text in generate() do something with it in parse(), and
ParseMeDo will take care of the rest :)


Happy Parsing!
