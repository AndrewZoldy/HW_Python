import pandas as pd
import argparse
from Bio import SeqIO

class Kmer_info:


    count = 0
    sequence = ''

    def __init__(self, kmer_name):
        self.sequence = kmer_name
        self.pos = []

    def counter(self):
        self.count += 1

    def position(self, index):
        self.pos.append(index)


def kmer_finder(file, size):
    
    sequence = SeqIO.read(file, 'fasta')
    sequence = sequence.seq
    kmer_dict = {}
    seq_ln = len(sequence)
    
    for i in range(seq_ln-kmer_size+1):
        current_kmer = sequence[i:(i+kmer_size)]
        if current_kmer in kmer_dict:
            kmer_dict[current_kmer].counter()
            kmer_dict[current_kmer].position(i)
        else:
            kmer_dict[current_kmer] = Kmer_info(current_kmer)
            kmer_dict[current_kmer].counter()
            kmer_dict[current_kmer].position(i)
    kmer_data = pd.DataFrame([])
    for current_kmer in kmer_dict.keys():
        kmer_data = kmer_data.append(pd.DataFrame({'kmer': str(kmer_dict[current_kmer].sequence),
                                               'number': kmer_dict[current_kmer].count,
                                               'positions': str(kmer_dict[current_kmer].pos)}, index=[1]), ignore_index=True)


    sort_kmer_data = kmer_data.sort_values(['number'], ascending=False)
    print(sort_kmer_data.iloc[[0]])

if __name__ == "__main__":
       
    parser = argparse.ArgumentParser(description='Script for finding kmers')
    parser.add_argument('-f', '--file', help='sequence', type=str, required=True)
    parser.add_argument('-s', '--size', help='kmer size', type=int, default=3)
    args = parser.parse_args()
    file = args.file
    size = args.size
    
    kmer_finder(file, size)

