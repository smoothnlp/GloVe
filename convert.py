from gensim.scripts.glove2word2vec import glove2word2vec
import sys

if __name__ == "__main__":
    input_vec = sys.argv[1]
    gensim_vec = sys.argv[2]

    glove2word2vec(glove_input_file=input_vec, word2vec_output_file=gensim_vec)
