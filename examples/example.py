import telnetservlib;

tns = telnetservlib.TelnetServer("127.0.0.1");
while True:
    tns.waitForConnection()
    tns.writeln(tns.query("Enter some text for me to repeat: "))
    tns.writeln("Goodbye!")
    tns.dropConnection()