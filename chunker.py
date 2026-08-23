def chunk(text, sz=200, ov=50):
    w = text.split()
    for i in range(0, len(w), sz - ov): yield ' '.join(w[i:i + sz])
