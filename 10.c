/* ex: set ff=dos ts=2 et: */
/* Copyright 2009 Ryan Flynn */
/*
 * The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
 * Find the sum of all the primes below two million.
 */

#include "miller-rabin.h"
#include <stdio.h>
#include <inttypes.h>

static void sum_primes_below(uint32_t n)
{
  uint64_t sum = 2 + 3;
  uint32_t i = 5;
  for (; i < n; i += 2)
    if (miller_rabin(i))
      sum += i;
  printf("%" PRIu64 "\n", sum);
}

int main(void)
{
  miller_rabin_init();
  sum_primes_below(10);
  sum_primes_below(2000000);
  return 0;
}

