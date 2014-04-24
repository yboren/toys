CFLAGS += -g
CXXFLAGS += -g

CLIB = libmyc.a

all : $(CLIB)

OBJS := $(patsubst %.c,%.o,$(wildcard *.c))
OBJS += $(patsubst %.cpp,%.o,$(wildcard *.cpp))
OBJS += $(patsubst %.cc,%.o,$(wildcard *.cc))

$(CLIB) : $(OBJS)
	ar rcs $@ $^

%.o : %.c
	$(CC) $(TOYS_INC) -c $^ -o $@

%.o : %.cc
	$(CXX) $(TOYS_INC) $^ -o $@

%.o : %.cpp
	$(CXX) $^ -o $@

% : %.o
	$(CC) $(LDFLAGS) $(TOYS_LIB) $^ -o $@

.PHONY : all clean

clean :
	rm -f $(CLIB) $(OBJS)
