# Instructions

Running this script should be super simple.  I didn't use any external libraries.  You should just need to run one line from the shell.  Please note that Python 3.6 should be used, because I've used some of the newer features of the language, like fstrings.

```
python main.py
```

To test class properties, you can run the following command.

```
python test.py
```

I've included the git repo so you can see my progress as I worked through this.  Some of the OOP approach might seem verbose, but the previous test I submitted for the web development job apparently had some shortcomings, and I wanted to show that I can use classes, etc.

# Assumptions

Please let me know if any of these were incorrect assumptions.

1. The input data would be well formed, just like the test-file that was provided to me, ie there would not be records short or extra of a field.
2. The input data file would be able to be read into memory and handled as such without chunking or managing.
3. 100.1 would be the same as 100.10.  I thought about how to get Python to ouput a "fixed" decimal output, but the best I could come up with would be string output, and I thought that would be less desirable than numerical data when parsed by an API or whatever comes next.
4. My code is readable and does not need a great deal of explanation.  I try to write code that reads like a narrative and therefore is easy to trace and debug.
5.  Lastly, I assumed that I could treat this programming exercise as I do with anything else, and use the powers of Google to learn anything I don't know, in this particular case - how to use an .xsd document to validate XML.

Thanks you for the chance to prove what I know, and I hope to hear from you soon!
