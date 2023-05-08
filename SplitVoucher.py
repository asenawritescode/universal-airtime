def split_voucher( code ) -> list:
    """
    Split the voucher code into two halves

    Parameters:
    ----------
    voucher: str
        The voucher code
    
    Returns:
    -------
    left, right : list
    """
    code = str(code)
    left, right = code[:len(code)//2], code[len(code)//2:]

    return left, right