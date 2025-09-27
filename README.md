# second_interview

* [要求](https://temporal-buttercup-ad0.notion.site/Second-Interview-27835c06f1fa80b0bb62ce06a4d0e750?pvs=73)
* [项目源代码](https://github.com/PKU-SDS-lab/POQD-ICML25)


## 关键词
* Multi-Vector Retrieval(MVR)
* Information Retrieval(IR)
* Query Decomposition -> Multi-hop QA
* LLM-based Optimizer

## 主要做了什么工作
* 提出了POQD的query decomposition framework for MVR
* 提出了一个用于端对端的end2end训练算法

## 解决了什么问题
* Query Decomposition&Embedding
  * [ColBERT](paper/colbert.pdf)&[ColBERT V2](paper/colbert_v2.pdf) [ColBERT博客讲解](https://blog.csdn.net/weixin_44839084/article/details/139184272)
  * [KELDaR](paper/KELDaR.pdf)
  * **解决方案**: train a model for searching the decomposed sub-queries that can optimize the downstream performance
    * The search process is non-differentiable, as sub-queries cannot propagate gradients from the downstream performance score [LLM_optimizer](paper/LLM_optimizer.pdf)
    * Evaluating candidate sub-queries requires trainining downstream RAG models, which is computationally expensive

## 问题列表
1. 为什么子查询不可微分呢？
2. 传统RAG中，数学部分，例如梯度如何传递，loss函数等内容
3. ColBERT如何工作，MaxSim如何工作
4. 为什么只训练生成器，不训练检索器呢？[Seven Failure Points on RAG](paper/failure_point_rag.pdf)

## 理论分析&理论
* 假设
  * [Polyak-Łojasiewicz star](paper/2003.00307v2.pdf)
  * [GaLore](paper/GaLore.pdf)

## 实验
* Baseline
  * Conventional dense retrieval encodes each query and document with one single embedding
  * ColBERT
  * Supervised Query Decomposition(**S-QD for short**)
  * Unsupervised Query Decomposition(**U-QD for short**)
  * In-Context Learning-based Query Decomposition(**ICL-QD for short**)
  * In-Context Learning with Feedback for Query Decomposition(**ICLF-QD**)