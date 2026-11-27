
<h2>什么是 Terraform？</h2>
<p><strong>Terraform</strong> 是目前最主流的<strong>基础设施即代码（IaC）</strong>工具。通过声明式的配置文件，你可以自动化管理云服务器、网络和数据库。</p>

<h2>为什么企业都在用它？</h2>
<ul>
    <li><strong>多云支持</strong>：一套语法管理 AWS、阿里云、腾讯云等。</li>
    <li><strong>幂等性</strong>：多次执行结果一致，安全可靠。</li>
    <li><strong>变更预览</strong>：执行 <code>terraform plan</code> 可以提前看到影响范围。</li>
</ul>

<h2>Ansible 的 5 ⼤核⼼功能</h2>
<ul>
    <li><strong>1 免Agent 架构（Agentless）</strong>：：Ansible 不需要你在被管理的远程服务器上安装任何客⼾端软件（Agent）。它完全基于原⽣的 SSH 协议（Windows 上基于
    WinRM）进⾏通信，控制机把任务转换成 Python 脚本推送到远程执⾏，执⾏完后⾃动清理。这极⼤地减少了维护负担。</li>
    <li><strong>2 幂等性（Idempotency）</strong>：这是运维⼯具的灵魂。幂等性意味着“多次运⾏同⼀个任务，结果完全⼀样”。如果服务器上已经安装了 Nginx 并且运⾏正常，
    你再次运⾏ Ansible 时它什么都不会做（显⽰ changed=0）；只有当配置⽂件被修改了，它才会去更新并重启服务。</li>
    <li><strong>3 ⼈类可读的 YAML 剧本（Playbooks）</strong>：Ansible 的任务编排⽂件被称为 Playbook（剧本），采⽤ YAML 格式编写。结构清晰、直观，即使是不懂复杂编程语⾔的运维⼈员也能快速上⼿。</li>
    <li><strong>4 丰富的模块⽣态（Rich Modules）</strong>：Ansible 提供了数千个内置模块（如 apt/yum管理软件包、copy传输⽂件、service管理服务、user管理账号），你不需要⼿写复杂的 Shell 脚本，直接调⽤模块即可。</li>
    <li><strong>5 处理程序（Handlers）与事件机制</strong>：Handlers 类似于触发器。⽐如只有当 Nginx 的配置⽂件发⽣改变时，才触发“重启 Nginx”的操作，如果没有改变则不重启，避免了不必要的服务中断。</li>
</ul>