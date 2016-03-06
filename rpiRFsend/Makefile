all: rpiRFsend

rpiRFsend: RCSwitch.o rpiRFsend.o
	$(CXX) $(CXXFLAGS) $(LDFLAGS) $+ -o $@ -lwiringPi

clean:
	$(RM) *.o rpiRFsend
