/* ex: set ff=dos ts=2 et: */
/* Copyright 2009 Ryan Flynn */
/*
 * Find the 10001st prime.
 */

#include "miller-rabin.h"
#include <stdio.h>

static void nth_prime(unsigned nth)
{
  unsigned cnt = 2,
           i = 3;
  for (; i > 1 && cnt <= nth; i += 2)
    if (miller_rabin(i))
      printf("%u ", i), ++cnt;
  fputc('\n', stdout);
}

int main(void)
{
  nth_prime(6);
  nth_prime(10001);
	return 0;
}

