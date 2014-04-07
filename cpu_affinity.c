#define _GNU_SOURCE
#include <sched.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>

int print_cpu_affinity()
{
	int i = 0;
	cpu_set_t cpu_mask;

	if(sched_getaffinity(0, sizeof(cpu_set_t), &cpu_mask) == -1)
	{
		printf("get_cpu_affinity fail, %s\n", strerror(errno));
		return -1;
	}
	
	printf("cpu affinity: ");
	for(i = 0; i < CPU_SETSIZE; i++)
	{
		if(CPU_ISSET(i, &cpu_mask))
			printf("%d ", i);
	}
	printf("\n");
	return 0;
}

int set_cpu_affinity(uint32_t cpu_affinity)
{
	int i = 0;
	cpu_set_t cpu_mask;

	CPU_ZERO(&cpu_mask);
	for(i = 0;cpu_affinity; i++, cpu_affinity >>= 1)
	{
		if(cpu_affinity & 1)
		{
			CPU_SET(i, &cpu_mask);
		}
	}
	if(sched_setaffinity(0, sizeof(cpu_set_t), &cpu_mask) == -1)
	{
		printf("set_cpu_affinity fail, %s\n", strerror(errno));
		return -1;
	}

	return 0;
}

void hold()
{
	while(1)
	{
;
	}
}

int main(int argc, char **argv)
{
	uint32_t cpu_affinity = 10;

	if( argc < 2 )
	{
		printf("no affinity given, use cpu_affinity = 10\n");
	}
	else
	{
		cpu_affinity = strtoul(argv[1], NULL, 2);
	}

	print_cpu_affinity();

	set_cpu_affinity(cpu_affinity);
	
	print_cpu_affinity();

	hold();

	return 0;
}
