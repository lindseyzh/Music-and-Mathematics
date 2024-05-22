# 音乐与数学大作业报告（音乐生成部分）

## 概述

本次大作业中，我们参考课堂内容和 Martin Gardner 的 Fractal Music, Hypercards and More，采用基于规则的方法生成随机音乐。我们选择音高和时值作为随机音乐的基本要素，使用 `music21` 库实现了白色、棕色、粉色音乐的生成器。我们将生成器的代码放在了 `music_gen/` 文件夹中，可以通过构造指定的生成器实例，生成任意长度、音域的音乐。

在介绍生成不同音乐的算法前，我们将生成的随机音乐抽象成音高和时值的序列，分别记为 $P_1, P_2, \ldots, P_n$ 和 $D_1, D_2, \ldots, D_n$。而随机音乐的生成算法，考虑的就是在已知 $(P_i, D_i)$ 的情况下，如何生成 $(P_{i+1}, D_{i+1})$。

## 白色音乐的生成

白色音乐是颜色音乐中相关性最低的一种。其中每一步的 $(P_{i+1}, D_{i+1})$ 都是独立生成，与 $(P_i, D_i)$ 无关。我们给出白色音乐的生成算法的伪代码：

```text
function WhiteNoiseGen(N, PitchList, DurationList):
    P = []
    D = []
    for i = 1 to N:
        P.Append(Random(PitchList))
        D.Append(Random(DurationList))
    return P, D
```

## 棕色音乐的生成

棕色音乐是一种相关性较强的音乐。在生成 $(P_{i+1}, D_{i+1})$ 时，首先在给定范围内随机生成音高和时值的变化量，即 $\Delta P_i$ 和 $\Delta D_i$，然后计算

$$(P_{i+1}, D_{i+1}) = (P_i + \Delta P_i, D_i + \Delta D_i)$$

我们给出棕色音乐的生成算法的伪代码：

```text
function BrownNoiseGen(N, StartPitch, StartDuration):
    P = [StartPitch]
    D = [StartDuration]
    for i = 2 to N:
        DeltaP = RandomPitchDelta(P[i-1])
        DeltaD = RandomDurationDelta(D[i-1])
        P.Append(P[i-1] + DeltaP)
        D.Append(D[i-1] + DeltaD)
    return P, D
```

值得一提的是，该算法并不要求当前处于不同的 $(P_i, D_i)$ 时，共享相同的变化量范围。因此当 $P_i$ 或 $D_i$ 已经到达边界时（可能是钢琴琴键的边界），我们可以通过改变变化量范围，保证 $(P_{i+1}, D_{i+1})$ 仍然在合法范围内。

## 粉色音乐的生成

粉色音乐的相关性介于白色音乐和棕色音乐之间。关于粉色音乐的生成算法，我们以音高的生成为例。我们给出 $k$ 维向量 $Dice = (d_1, d_2, \ldots, d_k)$ ，其中 $d_i, i = 1, 2, \ldots, k$ 的取值范围是 $0, 1,\ldots, K$。在生成 $P_{i+1}$ 时，比较 $i$ 和 $i+1$ 在二进制表示下的每一位，如果不同，则重新选择 $Dice$ 这一分量的值，最终由 $Dice$ 各个分量的和决定 $P_{i+1}$。我们给出粉色音乐的生成算法的伪代码：

```text
function PinkNoiseGen(N, PitchDice, DurationDice, PitchList, DurationList):
    P = [PitchList[Sum(PitchDice)]]
    D = [DurationList[Sum(DurationDice)]]
    for i = 2 to N:
        for j = 1 to k:
            if (GetBit(i, j) != GetBit(i-1, j)):
                PitchDice[j] = Random(K)
                DurationDice[j] = Random(K)
        P.Append(PitchList[Sum(PitchDice)])
        D.Append(DurationList[Sum(DurationDice)])
    return P, D
```

## 总结

该部分的工作主要是具体实现上述算法和基于已有的库（`music21`）构建音乐生成器。我们通过调整生成器的参数，生成了大量不同颜色、不同音域、不同长度的音乐，并通过比较这些音乐，感受到了白色、棕色、粉色音乐在相关性上的差异。

*PS: 这些生成算法基本上是来自于课上的PPT，在想法上感觉没什么新意（但是可以凑字数），因此这一部分的内容呈现到最终报告中时可以随意修改和删减。此外，我想不到这一部分还有什么可写的，如果关于这部分有新的可以写到报告里的想法，请告诉我，我会补充上去。*
