import telnetservlib

tns = telnetservlib.TelnetServer("127.0.0.1");
while True:
    tns.waitForConnection()
    answer, _ = tns.query("Enter some text for me to repeat: ")
    tns.writeln(answer)
    tns.writeln("Goodbye!")
    tns.dropConnection()