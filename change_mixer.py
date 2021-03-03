import lxml.etree as etree

do_volume = True
do_boost = False
do_mic1 = True
do_mic2 = True
AMPL = 5
BOOST = 1

filein = './mixer_paths_0.xml'
fileout = './mixer_paths_0_python.xml'

def volume(val_str):    
    val = int(val_str)
    return f'{val*AMPL}'

def boost(val_str):
    val = int(val_str)
    return f'{val+BOOST}'

parser = etree.XMLParser(remove_blank_text=False)

root = etree.parse(filein, parser)

# breakpoint()

if do_volume:
    if do_mic1:
        for mic in root.xpath("//ctl[@name='MIC1 Volume']"):
            attr = mic.attrib
            attr['value'] = volume(attr['value'])

    if do_mic2:
        for mic in root.xpath("//ctl[@name='MIC2 Volume']"):
            attr = mic.attrib
            attr['value'] = volume(attr['value'])

if do_boost:
    if do_mic1:
        for mic in root.xpath("//ctl[@name='MIC1 Boost Volume']"):
            attr = mic.attrib
            attr['value'] = boost(attr['value'])

    if do_mic2:
        for mic in root.xpath("//ctl[@name='MIC2 Boost Volume']"):
            attr = mic.attrib
            attr['value'] = boost(attr['value'])


# print(etree.tostring(root, pretty_print=True))

root.write(fileout, encoding="UTF-8", pretty_print=False,
                strip_text=False, with_tail=True)
