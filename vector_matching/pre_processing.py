import pyxem as pxm
import matplotlib.pyplot as plt


def get_peaks(dp: pxm.signals.ElectronDiffraction2D, **kwargs) -> pxm.signals.DiffractionVectors:
    """
    Get DiffractionVectors2D object from a dataset. 

    """
    st = dp.template_match_disk(disk_r = 2.2, subtract_min = False)
    vectors = st.get_diffraction_vectors(**kwargs)
    return vectors


def plot_peaks(dp: pxm.signals.ElectronDiffraction2D, **kwargs) -> None:
    st = dp.template_match_disk(disk_r = 2.2, subtract_min = False)
    vectors = st.get_diffraction_vectors(**kwargs)
    m = vectors.to_markers(sizes = 5, color = 'red')

    dp.plot(cmap='viridis_r',norm='log',title='',colorbar=False,
             scalebar=True,scalebar_color='black', axes_ticks='off')
    dp.add_marker(m)

    plt.tight_layout()
    plt.show()


