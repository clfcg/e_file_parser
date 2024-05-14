from lxml import etree


def get_stats(path):
    root = etree.parse(path)

    akts = root.xpath('.//AKT')
    zaps = root.xpath('.//ZAP')
    stats = {}
    stats['akt_count'] = len(akts)
    stats['zap_count'] = len(zaps)
    not_empty_akts = 0
    akt_nums = []
    for akt in akts:
        if akt[3].tag == 'N_EXP' and akt[6].tag == 'NOT_OPL_SUM':
            if int(akt[3].text) > 1 and int(akt[6].text.replace('.', '')) > 0:
                not_empty_akts += 1
                akt_nums.append(akt[0].text)
        else:
            stats['err'] = 'Ошибка в расположении тегов'
            break
    stats['not_empty_akts'] = not_empty_akts
    stats['not_empty_akts_num'] = akt_nums
    return stats