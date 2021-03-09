import lxml.etree as etree

filein = './mixer_paths_0.xml'
fileout = './mixer_paths_0_python.xml'


def volume(val_str, mic_gain):
    val = int(val_str)
    return f'{val*mic_gain}'


def boost(val_str, mic_boost):
    val = int(val_str)
    return f'{val+mic_boost}'


def main(mic1_gain, mic2_gain):
    do_volume = False
    do_boost = False

    if mic1_gain != -1:
        do_mic1 = True
        do_volume = True
    else:
        do_mic1 = False    
    
    if mic2_gain != -1:
        do_mic2 = True
        do_volume = True
    else:
        do_mic2 = False    
    
    # breakpoint()
    parser = etree.XMLParser(remove_blank_text=False)

    root = etree.parse(filein, parser)

    # breakpoint()

    if do_volume:
        if do_mic1:
            for mic in root.xpath("//ctl[@name='MIC1 Volume']"):
                attr = mic.attrib
                attr['value'] = volume(attr['value'], mic1_gain)

        if do_mic2:
            for mic in root.xpath("//ctl[@name='MIC2 Volume']"):
                attr = mic.attrib
                attr['value'] = volume(attr['value'], mic2_gain)

    if do_boost:
        if do_mic1:
            for mic in root.xpath("//ctl[@name='MIC1 Boost Volume']"):
                attr = mic.attrib
                attr['value'] = boost(attr['value'], 1)

        if do_mic2:
            for mic in root.xpath("//ctl[@name='MIC2 Boost Volume']"):
                attr = mic.attrib
                attr['value'] = boost(attr['value'], 1)


    # print(etree.tostring(root, pretty_print=True))

    root.write(fileout, encoding="UTF-8", pretty_print=False,
            strip_text=False, with_tail=True)


if __name__ == "__main__":
    import argparse
    # from six import text_type

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        '-m', '--mic1_gain',
        dest='mic1_gain',
        type=int,
        default=-1,
        help='specifies the gain for mic 1',
    )
    parser.add_argument(
        '-M', '--mic2_gain',
        dest='mic2_gain',
        type=int,
        default=-1,
        help='specifies the gain for mic 2',
    )

    args, unknown = parser.parse_known_args()

    try:
        main(
            args.mic1_gain,
            args.mic2_gain,
        )
    except KeyboardInterrupt:
        pass
    finally:
        print("Done\n")
