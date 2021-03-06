from dataloaders.vcr import VCR
from utils.extractionKeyword import extractionKeyword
from utils.extractionKnowledge import extractionKnowledge
from utils.topKknowledge import topKknowledge
import time # this is test
import torch


train_answer = VCR('train','answer')
train_rationale = VCR('train','rationale')
val_answer = VCR('val','answer')
val_rationale = VCR('val', 'rationale')
#test_answer = VCR('test','answer')
#test_rationale = VCR('test', 'rationale')

# definee keyword extractor
keywordExtractor = extractionKeyword()
# define knowledge extractor
knowledgeExtractor = extractionKnowledge(5,10)
# define topK extractor
topKExtractor = topKknowledge(50,10)

print('start!!!') # this is test
start = time.time() # this is test
k = 0

for t_answer,t_rationale in zip(train_answer,train_rationale):
    answer_list = []
    rationale_list = []
    print('k : ',k)
    k += 1
    for i in range(4):
        knowledgeExtractor.get_knowledge(keywordExtractor.get_keyword(t_answer['answer_list'][i]))
        knowledgeExtractor.get_knowledge(keywordExtractor.get_keyword(t_rationale['answer_list'][i]))
        #answer_list.append(knowledgeExtractor.get_knowledge(keywordExtractor.get_keyword(t_answer['answer_list'][i])))
        #rationale_list.append(knowledgeExtractor.get_knowledge(keywordExtractor.get_keyword(t_rationale['answer_list'][i])))

end = time.time() # this is test
print('time : ',end-start) # this is test
'''
#start = time.time() # this is test
for v_answer,v_rationale in zip(val_answer,val_rationale):
    answer_list = []
    rationale_list = []
    for i in range(4):
        answer_list.append(knowledgeExtractor.get_knowledge(keywordExtractor.get_keyword(v_answer['answer_list'][i])))
        #rationale_list.append(knowledgeExtractor.get_knowledge(keywordExtractor.get_keyword(t_rationale['answer_list'][i])))

'''
#end = time.time() # this is test
#print('time : ',end-start) # this is test
