def padding(image : ndarray, wantedshape : Tuple[int, int]): #wanted shape should be bigger than image shape
    curshape = image.shape
    if curshape >= wantedshape:
        return
    yDiff = wantedshape[0] - curshape[0]
    xDiff = wantedshape[1] - curshape [1]
    leftoverX = xDiff % 2
    leftoverY = yDiff % 2
    for i in range(xDiff//2):
        image = np.insert(image, 0, 0, axis = 1)
        image = np.append(image, [[[0, 0, 0]] for i in range(image.shape[0])], axis = 1)
    
    for i in range(yDiff//2):
        pad = np.array([[[0, 0, 0]]*image.shape[1]])
        image = np.vstack((image, pad))
        image = np.vstack((pad, image))
        
    if leftoverX:
        image = np.insert(image, 0, 0, axis = 1)
    if leftoverY:
        pad = np.array([[[0, 0, 0]]*image.shape[1]])
        image = np.vstack((image, pad))
    
    return image 
