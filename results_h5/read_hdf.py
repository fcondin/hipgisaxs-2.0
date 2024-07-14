import numpy as np
import matplotlib.pyplot as plt
import h5py


def main():
    path_to_hf_file = r'../gisaxs.h5'
    # f = h5py.File(r'cylinder_test.h5', 'r')
    with h5py.File(path_to_hf_file, 'r') as f:
        data = f['cylinder']
        print(data)
        # data = np.abs(data)
        re_part = np.real(data)
        im_part = np.imag(data)

        # the_shape = np.shape(np.real(data))
        # data = np.random.randn(*the_shape)
        # ans = f.keys()
        # print(ans)

        plt.figure('real')
        plt.imshow(re_part, cmap='RdBu_r')  # RdBu
        plt.figure('imaginary')
        plt.imshow(im_part, cmap='RdBu_r')  # RdBu
        # plt.figure('random')
        # plt.imshow(data, cmap='binary')
        plt.show()
    return 2


if __name__ == '__main__':
    main()
