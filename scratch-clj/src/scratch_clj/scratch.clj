(ns scratch-clj.scratch
  (:require [clojure.string :as str]
            [clojure.edn :as edn]
            [clojure.java.io :as io]
            [clojure.data.json :as json]
            [clojure.set :as set]))

(defn vec-remove
  "remove elem in coll"
  [coll pos]
  (vec (concat (subvec coll 0 pos) (subvec coll (inc pos)))))

(def excel-whitelisted-genomes
  (apply vector
         (apply hash-set (map
                          (fn [x]
                            (first
                             (str/split x #"\t")))
                          (str/split-lines
                           (slurp "../genomes-abhi-list.txt"))))))

(def excel-redlisted-genomes
  (apply vector
         (apply hash-set (map
                          (fn [x]
                            (first
                             (str/split x #"\t")))
                          (str/split-lines
                           (slurp "../genomes-ena-list.txt"))))))

(def excel-yellowlisted-genomes
  (vec-remove
   (apply vector
          (apply hash-set (map
                           (fn [x]
                             (first
                              (str/split x #"\t")))
                           (str/split-lines
                            (slurp "../genomes-em-list.txt"))))) 17))

(comment
  (first excel-whitelisted-genomes)
  (last excel-whitelisted-genomes)
  (first excel-redlisted-genomes)
  (last excel-redlisted-genomes)
  (first excel-yellowlisted-genomes)
  (last excel-yellowlisted-genomes))

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
  (last genomes-in-abhi-folder)
  (first genomes-in-em-folder)
  (last genomes-in-em-folder)
  (first genomes-in-ena-folder)
  (last genomes-in-ena-folder))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; NOTE duplicates
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(def all-downloaded-genomes)

(clojure.set/intersection
 (apply hash-set genomes-in-abhi-folder)
 (apply hash-set genomes-in-em-folder))

(clojure.set/intersection
 (apply hash-set genomes-in-abhi-folder)
 (apply hash-set genomes-in-ena-folder))

(clojure.set/intersection
 (apply hash-set genomes-in-em-folder)
 (apply hash-set genomes-in-ena-folder))

(def all-excel-listed-genomes)

(clojure.set/intersection
 (apply hash-set excel-whitelisted-genomes)
 (apply hash-set excel-redlisted-genomes))

(clojure.set/intersection
 (apply hash-set excel-whitelisted-genomes)
 (apply hash-set excel-yellowlisted-genomes))

(clojure.set/intersection
 (apply hash-set excel-yellowlisted-genomes)
 (apply hash-set excel-redlisted-genomes))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; NOTE missing genomes
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


(clojure.set/difference
 (apply hash-set excel-whitelisted-genomes)
 (apply hash-set genomes-in-abhi-folder))

(clojure.set/difference
 (apply hash-set genomes-in-abhi-folder)
 (apply hash-set excel-whitelisted-genomes))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; NOTE all genomes files
;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(count
 (clojure.set/union
  (apply hash-set genomes-in-abhi-folder)
  (apply hash-set genomes-in-ena-folder)
  (apply hash-set genomes-in-em-folder)))

(def all-genomes
  (apply vector
         (partition 2
         (str/split-lines
          (slurp "../_list_of_all_genomes_files.txt")))))

(comment
  (first all-genomes)
  (last all-genomes)
)


(spit (str "../lab/" "_list_of_all_genomes_files.json")
      (json/write-str all-genomes))

(count all-genomes)



;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; NOTE all lab genome files
;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(def all-lab-genomes
  (apply vector
         (partition 2
                    (str/split-lines
                     (slurp "../lab/_all_lab_genome_files.txt")))))

(comment
  (first all-lab-genomes)
  (last all-lab-genomes)
)


(spit (str "../lab/" "_all_lab_genome_files.json")
      (json/write-str all-lab-genomes))

(count all-lab-genomes)





