
class Phonetic():
    ''' Process phonetic symbols of Chiese characters
    or other languages.
    '''
    def replace(self,phonestr,tone):

        if tone=='5':
            return phonestr
        arry_a = ['ā', 'á', 'ǎ', 'à']
        arry_o = ['ō', 'ó', 'ǒ', 'ò']
        arry_e = ['ē', 'é', 'ě', 'è']
        arry_i = ['ī', 'í', 'ǐ', 'ì']
        arry_u = ['ū', 'ú', 'ǔ', 'ù']
        arry_v = ['ǖ', 'ǘ', 'ǚ', 'ǜ']
        #arry_A = ['Ā', 'Á', 'Ǎ', 'À']
        #arry_O = ['Ō', 'Ó', 'Ǒ', 'Ò']
        #arry_E = ['Ē', 'É', 'Ě', 'È']
        if 'iu' in phonestr :
            return string.replace(phonestr,'u',arry_u[int(tone)-1],maxsplit=1)
        if 'ui' in phonestr:
            return string.replace(phonestr,'i',arry_i[int(tone)-1],maxsplit=1)
        if 'a' in phonestr:
            return string.replace(phonestr,'a',arry_a[int(tone)-1],maxsplit=1)
        if 'o' in phonestr:
            return string.replace(phonestr,'o',arry_o[int(tone)-1],maxsplit=1)
        if 'e' in phonestr:
            return string.replace(phonestr,'e',arry_e[int(tone)-1],maxsplit=1)
        if 'i' in phonestr :
            return string.replace(phonestr,'i',arry_i[int(tone)-1],maxsplit=1)
        if 'u' in phonestr:
            return string.replace(phonestr,'u',arry_u[int(tone)-1],maxsplit=1)
        if 'v' in phonestr:
            return string.replace(phonestr,'v',arry_v[int(tone)-1],maxsplit=1)

        return phonestr
