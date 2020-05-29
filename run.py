from dataloaders.vcr import VCR
from extractionKeyword import extractionKeyword
from extractionKnowledge import extractionKnowledge

train_answer = VCR('train','answer')
train_rationale = VCR('train','rationale')
#val_answer = VCR('val','answer')
#val_rationale = VCR('val', 'rationale')
#test_answer = VCR('test','answer')
#test_rationale = VCR('test', 'rationale')

keywordExtractor = extractionKeyword()
knowledgeExtractor = extractionKnowledge(50,10)

for t_answer,t_rationale in zip(train_answer,train_rationale):
    answer_list = []
    rationale_list = []
    for i in range(4):
        answer_list.append(keywordExtractor.get_keyword(t_answer['answer_list'][i]))
        rationale_list.append(keywordExtractor.get_keyword(t_rationale['answer_list'][i]))
    keywordExtractor.get_keyword(t_answer['question'])
    keywordExtractor.get_keyword(t_rationale['question'])

