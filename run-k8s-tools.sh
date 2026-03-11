#!/bin/bash
# 调用 k8s-tools：优先用 PATH，否则用默认路径（sh 调用时通常未加载 shell 配置）
# 用法: ./run-k8s-tools.sh <命令> [参数...]
# 示例: ./run-k8s-tools.sh k8s-tools exec -c=genesis-admarketing -- ./genesis -h
# 也可整段传入: sh run-k8s-tools.sh "exec -c=genesis-admarketing -- ./genesis -h"

if command -v k8s-tools &>/dev/null; then
    K8S_TOOLS_BIN="k8s-tools"
else
    K8S_TOOLS_BIN="${K8S_TOOLS_BIN:-/Users/qimao/k8s-tools}"
    [[ ! -x "$K8S_TOOLS_BIN" ]] && { echo "错误: 未找到 k8s-tools（PATH 与默认路径均不可用）"; exit 1; }
fi

if [[ $# -eq 0 ]]; then
    echo "用法: $0 <命令> [参数...]"
    echo "示例: $0 k8s-tools exec -c=genesis-admarketing -- ./genesis -h"
    exit 1
fi

# 若第一个参数是 k8s-tools 或 /k8s-tools，则用 k8s-tools 执行后续参数
if [[ "$1" == "k8s-tools" || "$1" == "/k8s-tools" ]]; then
    exec "$K8S_TOOLS_BIN" "${@:2}"
fi

# 若只有一个参数且以 exec 开头，视为 k8s-tools 的参数（兼容整段传入）
# 例: sh run-k8s-tools.sh "exec -c=genesis-admarketing -- ./genesis -h"
if [[ $# -eq 1 && "$1" == exec* ]]; then
    exec "$K8S_TOOLS_BIN" $1
fi

exec "$@"
