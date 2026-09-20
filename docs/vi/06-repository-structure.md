# 06 — Cấu trúc repository và các vị trí cài đặt được đề xuất

Cây thư mục dưới đây là **kiến trúc mục tiêu**, không phải yêu cầu phải tạo mọi thư mục và file placeholder ở v0.1. Runtime viết bằng Python. Method chủ yếu dùng Markdown/YAML và phải được đóng gói thành resource có thể truy cập sau khi cài, không được giả định user sẽ giữ mãi source repository đã clone.

## Framework repository — cấu trúc mục tiêu

```text
aelc/
├── README.md
├── AGENTS.md
├── setup.sh                      # bootstrap macOS/Linux
├── setup.ps1                     # bootstrap Windows PowerShell
├── pyproject.toml
├── uv.lock                       # nếu quyết định dùng uv lock
├── .python-version               # nếu chốt Python version
├── src/
│   └── aelc/
│       ├── __init__.py
│       ├── __main__.py
│       ├── core/                  # config, context, domain types
│       ├── identity/              # canonical member, provider mapping
│       ├── membership/            # project role và access
│       ├── sessions/              # attribution và session context
│       ├── knowledge/             # member state, freshness, coverage
│       ├── evidence/              # claim provenance, verification
│       ├── accountability/        # risk, debt, human approval
│       ├── capabilities/          # interface document/task/... độc lập provider
│       ├── integrations/          # adapter MCP / REST / local
│       ├── harness/               # adapter contracts và context builder
│       ├── installer/             # detection, manifest, install/update
│       ├── storage/               # SQLite và interface remote tương lai
│       └── cli/                   # các lệnh aelc
├── method/
│   ├── principles/
│   ├── protocols/
│   ├── workflows/
│   │   ├── codebase_understanding/
│   │   ├── onboarding/
│   │   ├── greenfield/
│   │   ├── feature/
│   │   └── bugfix/
│   ├── roles/
│   ├── agents/
│   └── templates/
├── harnesses/
│   ├── claude_code/
│   ├── codex/
│   └── copilot/
├── templates/project/            # template .aelc/ tối thiểu
├── schemas/                      # các định dạng dữ liệu công khai, có version
├── tests/unit/
├── tests/integration/
├── docs/
└── scripts/
```

Trong mỗi Python domain module, có thể dùng `models.py`, `service.py`, `repository.py` và file provider-specific **khi có nhu cầu thực tế**. Không sinh file rỗng chỉ để khớp cây thư mục mục tiêu.

**Quyết định packaging cần chốt trước khi viết code:** Nếu `method/`, `harnesses/`, `templates/` nằm ở root, `pyproject.toml` phải đóng gói/cài đặt chúng rõ ràng như package resources. Một phương án khác là đặt resource chạy thực tế trong `src/aelc/resources/` và giữ docs cho human ở root. Cả hai đều đáp ứng yêu cầu đã thống nhất; xem [Quyết định mở](13-decisions-and-open-questions.md).

## Application project sau `aelc init` — minh họa

```text
payment-service/
├── existing-application-files...
├── .aelc/
│   ├── project.yaml              # canonical project config
│   ├── knowledge/                # verified knowledge có thể chia sẻ
│   ├── roles/                    # project role expectations
│   ├── policies/                 # constraints được human/team phê duyệt
│   ├── work/                     # shareable decisions/evidence references
│   └── local/                    # gitignored nếu cần local repo state
├── .claude/                      # tùy chọn: chỉ cấu hình harness cần thiết
└── .agents/                      # tùy chọn: chỉ cấu hình harness cần thiết
```

**Không** copy `src/aelc/`, `method/` hoặc toàn bộ framework source vào application project. Không ghi đè `AGENTS.md`, `CLAUDE.md`, `.claude/` hoặc project settings có sẵn. Global skills có thể đã đủ và project không cần tạo thêm thư mục riêng cho harness.

## Máy của user — minh họa

```text
USER_CONFIG_DIR/aelc/           # config + identity/session references
USER_DATA_DIR/aelc/             # SQLite/cache nếu sử dụng
USER_CREDENTIAL_STORE           # access/refresh tokens, lưu riêng
HARNESS_USER_SKILL_DIR/...      # global skills do AELC tạo
```

Xác định đường dẫn theo OS conventions và vị trí harness adapter hỗ trợ. `~/.config/aelc` trên Unix chỉ là ví dụ, không phải path cố định cho Windows.

## Phần cần cho MVP

Chỉ implement CLI, installer tối thiểu, identity/provider interface (GitHub + fallback có assurance thấp hơn nếu quyết định), membership, session context, local storage, project template tối thiểu và adapter `aelc-init`. Mở rộng cây thư mục theo nhu cầu sau khi end-to-end behavior và tests chứng minh cần thiết. Xem [MVP](11-mvp-v0.1.md).
