
 Esta proposta descreve um projeto de detecção e contagem de frutos de manga em imagens de árvores utilizando técnicas simples de segmentação baseadas em cor e textura. O objetivo é aplicar métodos de visão computacional para estimar o número de frutos em árvores fotografadas em ambiente real, com base em imagens RGB. O projeto se baseia no artigo de Payne et al. (2013), que demonstrou forte correlação entre contagens automatizadas e contagens manuais. 
A estimativa de produtividade de culturas como a mangueira é uma tarefa importante para planejamento agrícola e tomada de decisão. Tradicionalmente, essa estimativa é feita manualmente, sendo custosa e sujeita a erros. Com o avanço de técnicas de visão computacional, é possível automatizar esse processo. O presente projeto tem como objetivo desenvolver uma ferramenta simples para detecção e contagem de frutos de manga em imagens RGB de árvores, com base em segmentação por cor e textura.

Serão utilizadas imagens de árvores de manga obtidas em pomares, com câmera digital convencional (RGB). Caso não haja disponibilidade imediata de imagens reais, pretende-se utilizar um subconjunto de imagens públicas disponíveis na internet, ou então gerar imagens sintéticas com frutas semelhantes. A coleta das imagens será feita em ambiente externo, durante o dia, priorizando imagens com boa iluminação lateral.

A metodologia é baseada no artigo de Payne et al. (2013) e consiste nas seguintes etapas:

    Pré-processamento da imagem: redimensionamento e suavização;
    Segmentação por cor: transformação das imagens para os espaços de cor RGB e YCbCr;
    Segmentação por textura: identificação de regiões com alta variabilidade de pixels adjacentes;
    Contagem de frutos: contagem de blobs (regiões) detectadas após a segmentação;
    Avaliação da acurácia: comparação com contagens manuais em um conjunto de imagens anotadas.

As implementações serão feitas em Python utilizando a biblioteca OpenCV.
