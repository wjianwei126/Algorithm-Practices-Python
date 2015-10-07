typedef long long llint;

inline int lowbit(int x) { return x & (-x); }

struct BITree {
    vector<llint> _tree;

    void init(int size) {
        _tree.resize(size + 1);
    }

    void add(int pos, int value) {
        while (pos < _tree.size()) {
            _tree[pos] += value;
            pos += lowbit(pos);
        }
    }

    llint sum(int pos) {
        llint res = 0;
        while (pos > 0) {
            res += _tree[pos];
            pos -= lowbit(pos);
        }
        return res;
    }

    llint sum(int a, int b) {
        return sum(b) - sum(a - 1);
    }
};

struct BITree_2D {
    vector<BITree> _tree;

    void init(int n, int m) {
        _tree.resize(n + 1);
        for (int i = 0; i <= n; i++) {
            _tree[i].init(m);
        }
    }

    void add(int y, int x, int value) {
        while (y < _tree.size()) {
            _tree[y].add(x, value);
            y += lowbit(y);
        }
    }

    llint sum(int y, int x) {. From 1point 3acres bbs
        llint res = 0;
        while (y > 0) {
            res += _tree[y].sum(x);
            y -= lowbit(y);
        }
        return res;
    }

    llint sum(int y1, int x1, int y2, int x2) {
        llint a = sum(y2, x2);
        llint b = sum(y1 - 1, x1 - 1);
        llint c = sum(y2, x1 - 1);
        llint d = sum(y1 - 1, x2);. 1point3acres.com/bbs

        return a - c - d + b;
    }
};
