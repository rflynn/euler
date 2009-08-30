/* ex: set ff=dos ts=2 et: */
/* Copyright 2009 Ryan Flynn */
/*
 * Implement Miller-Rabin primality test
 */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>

/**
 * recursive, very simple version of the Miller-Rabin primality test.
 */
static uint32_t millertime(uint32_t a, uint32_t i, uint32_t n)
{
  uint32_t x, y;
  if (i == 0)
    return 1;
  x = millertime(a, i / 2, n);
  if (x == 0)
    return 0;
  y = ((uint64_t)x * x) % n;
  if (y == 1 && x != 1 && x != n - 1)
    return 0;
  if ((i & 1))
    y = ((uint64_t)a * y) % n;
  return y;
}

/**
 * "multiple Rabin tests using the first 7 primes (using 8 gives no improvement)
 * are valid for every number up to 3.4e10(sic)"
 * @ref http://mathworld.wolfram.com/Rabin-MillerStrongPseudoprimeTest.html
 */
int miller_rabin(uint32_t n)
{
  static const uint32_t a[] = { 2, 3, 5, 7, 11, 13 };
  unsigned i = 0;
  while (
    i < sizeof a / sizeof a[0] &&
    a[i] < n &&
    1 == millertime(a[i++], n - 1, n)
  );
  return sizeof a / sizeof a[0] == i || a[i] >= n;
}

void miller_rabin_init(void)
{
  printf("RAND_MAX=%u\n", RAND_MAX);
  assert(miller_rabin(2));
  assert(miller_rabin(3));
  assert( miller_rabin(5));
  assert(!miller_rabin(6));
  assert( miller_rabin(7));
  assert(!miller_rabin(10));
  assert(!miller_rabin(232));
  assert( miller_rabin(257));
  assert( miller_rabin(45821));
  assert( miller_rabin(45821));
  assert( miller_rabin(51539));
  assert( miller_rabin(63499));
  assert( miller_rabin(65521));
  assert( miller_rabin(65543));
  assert( miller_rabin(65537UL));
  assert( miller_rabin(70853UL));
  assert( miller_rabin(92431UL));
  assert( miller_rabin(104729UL));
  assert( miller_rabin(2146435153UL));
  assert(!miller_rabin((uint32_t)7 * 127 * 4830073)); /* 4293934897; highest uint32_t non-prime */
}



