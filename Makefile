CFLAG += -g
CXXFLAG += -g

BINARY = cpu_affinity

all : $(BINARY) 

%c.%o :
	$(CC) $^ -o $@

%cc.%o :
	$(CXX) $^ -o $@

%cpp.%o :
	$(CXX) $^ -o $@

.PHONY : all clean

clean :
	rm -f *.o $(BINARY)
