(ns scratch-clj.scratch
  (:require [clojure.string :as str]
            [clojure.set :as set]))

(defn vec-remove
  "remove elem in coll"
  [coll pos]
  (vec (concat (subvec coll 0 pos) (subvec coll (inc pos)))))

(def whitelisted-genomes
  (apply vector
         (apply hash-set (map
                          (fn [x]
                            (first
                             (str/split x #"\t")))
                          (str/split-lines
                           (slurp "../genomes-abhi-list.txt"))))))

(def redlisted-genomes
  (apply vector
         (apply hash-set (map
                          (fn [x]
                            (first
                             (str/split x #"\t")))
                          (str/split-lines
                           (slurp "../genomes-ena-list.txt"))))))

(def yellowlisted-genomes
  (vec-remove
   (apply vector
          (apply hash-set (map
                           (fn [x]
                             (first
                              (str/split x #"\t")))
                           (str/split-lines
                            (slurp "../genomes-em-list.txt"))))) 17))


(comment
  (first whitelisted-genomes)
  (first redlisted-genomes)
  (first yellowlisted-genomes)
)


(def genomes-in-abhi-folder
  (apply vector
         (apply hash-set (map
                          (fn [x]
                            (first (str/split x #"_")))
                          (str/split-lines
                           (slurp "../genomes_abhi/_list_of_files.txt"))))))

(def genomes-in-em-folder
  (apply vector
         (apply hash-set (map
                          (fn [x]
                            (first (str/split x #"_")))
                          (str/split-lines
                           (slurp "../genomes_em/_list_of_files.txt"))))))

(def genomes-in-ena-folder
  (apply vector
         (apply hash-set (map
                          (fn [x]
                            (first (str/split x #"_")))
                          (str/split-lines
                           (slurp "../genomes_ena/_list_of_files.txt"))))))

(comment
  (first genomes-in-abhi-folder)
  (first genomes-in-em-folder)
  (first genomes-in-ena-folder)
)



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; NOTE duplicates
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(def all-downloaded-genomes )


(clojure.set/intersection
(apply hash-set genomes-in-abhi-folder)
(apply hash-set genomes-in-em-folder))


(clojure.set/intersection
 (apply hash-set genomes-in-abhi-folder)
 (apply hash-set genomes-in-ena-folder))


(clojure.set/intersection
 (apply hash-set genomes-in-em-folder)
 (apply hash-set genomes-in-ena-folder))



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; NOTE duplicates
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;



(def all-excel-listed-genomes )

(clojure.set/intersection
 (apply hash-set whitelisted-genomes)
 (apply hash-set redlisted-genomes))

(clojure.set/intersection
 (apply hash-set whitelisted-genomes)
 (apply hash-set yellowlisted-genomes))

(clojure.set/intersection
 (apply hash-set yellowlisted-genomes)
 (apply hash-set redlisted-genomes))

