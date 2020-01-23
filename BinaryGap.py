import logging
logger = logging.getLogger(__name__)

# codility task https://app.codility.com/programmers/lessons/1-iterations/binary_gap/


class BinaryGapException(Exception):
    pass


def binary_gap(number):

    try:
        base2 = bin(number)
    except TypeError as e:
        raise BinaryGapException("my msg")

    #logging.debug("base2: ", base2)
    gaps = []
    gap = 0
    from1 = False
    for i in base2:
        if i == '1':
            if gap != 0:
                gaps.append(gap)
            gap = 0
            from1 = True
        if i == '0' and from1:
            gap += 1

    #logging.info("gaps: ", gaps)
    #print("gaps: %s" % gaps)
    if gaps:
        return max(gaps)
    else:
        return 0

