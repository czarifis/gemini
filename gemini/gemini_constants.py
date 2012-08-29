#!/usr/bin/env python

VARIANTS_KEY = "variant_id"
BUFFER_SIZE  = 10000


# genotype encoding.
# 0 / 00000000 hom ref
# 1 / 00000001 het
# 2 / 00000010 unknown
# 3 / 00000011 hom alt
GT_HOM_REF = 0
GT_HET = 1
GT_UNKNOWN = 2
GT_HOM_ALT = 3