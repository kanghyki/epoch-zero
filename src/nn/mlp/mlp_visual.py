import matplotlib.pyplot as plt

def draw_network(layer_sizes):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis('off')
    
    v_spacing = 1
    h_spacing = 2
    layer_count = len(layer_sizes)

    # 뉴런 위치 저장
    neuron_positions = []
    for layer_idx, num_neurons in enumerate(layer_sizes):
        layer_x = layer_idx * h_spacing
        top = v_spacing * (num_neurons - 1) / 2
        positions = [(layer_x, top - i * v_spacing) for i in range(num_neurons)]
        neuron_positions.append(positions)

    # 뉴런 그리기
    for layer in neuron_positions:
        for (x, y) in layer:
            circle = plt.Circle((x, y), 0.2, fill=True, color='skyblue', ec='k')
            ax.add_patch(circle)

    # 연결선 그리기
    for l1, l2 in zip(neuron_positions[:-1], neuron_positions[1:]):
        for (x1, y1) in l1:
            for (x2, y2) in l2:
                ax.plot([x1, x2], [y1, y2], 'gray', lw=0.5)

    plt.title("MLP structure visualization")
    plt.show()

draw_network([2, 4, 4, 4, 4, 1])
