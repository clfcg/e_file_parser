import copy
from pathlib import Path

from lxml import etree


def create_new_file(path):
    root = etree.parse(path)

    akts = root.xpath('.//AKT')
    out_e = etree.Element('PACKET')
    for akt in akts:
        if int(akt[3].text) > 1 and int(akt[6].text.replace('.', '')) == 0:
            zaps = akt.findall('ZAP')
            out_akt = etree.Element('AKT')
            for elem in akt:
                if elem.tag != 'ZAP':
                    out_akt.append(elem)
            for zap in zaps:
                out_akt.append(zap)
                out_e.append(copy.copy(out_akt))
                out_akt.remove(zap)
        else:
            out_e.append(akt)

    doc = etree.ElementTree(out_e)
    folder = Path(path).resolve().parent / 'new_file/'
    folder.mkdir(parents=True, exist_ok=True)
    out_efile = folder / Path(path).name
    doc.write(out_efile, pretty_print=True, encoding='windows-1251', xml_declaration=True)
